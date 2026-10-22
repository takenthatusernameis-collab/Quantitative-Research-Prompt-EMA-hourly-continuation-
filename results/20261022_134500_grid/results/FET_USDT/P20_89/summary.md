# EMA Hourly Continuation — FET/USDT P20_89

**Symbol:** FET/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.6386 |
| net_win_rate | 0.4739 |
| gross_profit_factor | 0.9213 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -3.6921 |
| sortino_ratio | -1.3266 |
| max_drawdown | 0.8090 |
| cagr | -0.4680 |
| net_avg_win | 45.4593 |
| net_avg_loss | -64.1328 |
| avg_hold_time_bars | 13.9463 |
| exposure | 0.4133 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
