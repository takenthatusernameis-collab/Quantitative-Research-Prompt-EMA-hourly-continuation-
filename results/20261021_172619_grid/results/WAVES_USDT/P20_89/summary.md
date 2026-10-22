# EMA Hourly Continuation — WAVES/USDT P20_89

**Symbol:** WAVES/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.7214 |
| net_win_rate | 0.4848 |
| gross_profit_factor | 0.9641 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -2.6878 |
| sortino_ratio | -0.9077 |
| max_drawdown | 0.6950 |
| cagr | -0.3422 |
| net_avg_win | 62.1725 |
| net_avg_loss | -81.0975 |
| avg_hold_time_bars | 14.2755 |
| exposure | 0.3627 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
