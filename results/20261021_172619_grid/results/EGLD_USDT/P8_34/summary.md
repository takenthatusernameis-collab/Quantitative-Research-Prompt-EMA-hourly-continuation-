# EMA Hourly Continuation — EGLD/USDT P8_34

**Symbol:** EGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 770 |
| net_profit_factor | 0.7291 |
| net_win_rate | 0.4883 |
| gross_profit_factor | 0.9848 |
| gross_win_rate | 0.4883 |
| sharpe_ratio | -3.0468 |
| sortino_ratio | -1.2102 |
| max_drawdown | 0.7611 |
| cagr | -0.4255 |
| net_avg_win | 53.7872 |
| net_avg_loss | -70.4001 |
| avg_hold_time_bars | 8.1494 |
| exposure | 0.2852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
