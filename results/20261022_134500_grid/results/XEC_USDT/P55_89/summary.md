# EMA Hourly Continuation — XEC/USDT P55_89

**Symbol:** XEC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.3311 |
| net_win_rate | 0.4181 |
| gross_profit_factor | 0.6876 |
| gross_win_rate | 0.4411 |
| sharpe_ratio | -7.6000 |
| sortino_ratio | -2.8397 |
| max_drawdown | 0.9725 |
| cagr | -0.7566 |
| net_avg_win | 16.5276 |
| net_avg_loss | -35.8679 |
| avg_hold_time_bars | 4.4296 |
| exposure | 0.1395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
