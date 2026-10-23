# EMA Hourly Continuation — GMT/USDT P20_144

**Symbol:** GMT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 538 |
| net_profit_factor | 0.5287 |
| net_win_rate | 0.4368 |
| gross_profit_factor | 0.7962 |
| gross_win_rate | 0.4442 |
| sharpe_ratio | -4.6642 |
| sortino_ratio | -1.5191 |
| max_drawdown | 0.8497 |
| cagr | -0.5171 |
| net_avg_win | 40.0585 |
| net_avg_loss | -58.7675 |
| avg_hold_time_bars | 20.6171 |
| exposure | 0.5042 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
