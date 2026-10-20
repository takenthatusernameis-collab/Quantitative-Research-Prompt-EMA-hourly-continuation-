# EMA Hourly Continuation — EUL/USDT P100_200

**Symbol:** EUL/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.4397 |
| net_win_rate | 0.4182 |
| gross_profit_factor | 0.6605 |
| gross_win_rate | 0.4209 |
| sharpe_ratio | -4.3041 |
| sortino_ratio | -1.1709 |
| max_drawdown | 0.7554 |
| cagr | -0.4277 |
| net_avg_win | 37.9255 |
| net_avg_loss | -62.0020 |
| avg_hold_time_bars | 8.2708 |
| exposure | 0.1402 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
