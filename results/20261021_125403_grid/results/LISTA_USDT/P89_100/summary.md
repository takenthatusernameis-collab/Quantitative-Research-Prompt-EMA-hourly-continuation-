# EMA Hourly Continuation — LISTA/USDT P89_100

**Symbol:** LISTA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 173 |
| net_profit_factor | 0.6159 |
| net_win_rate | 0.4682 |
| gross_profit_factor | 0.9065 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -2.1211 |
| sortino_ratio | -0.4141 |
| max_drawdown | 0.3830 |
| cagr | -0.1727 |
| net_avg_win | 70.7807 |
| net_avg_loss | -101.1835 |
| avg_hold_time_bars | 5.7168 |
| exposure | 0.0484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
