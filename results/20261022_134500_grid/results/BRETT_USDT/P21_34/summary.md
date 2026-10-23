# EMA Hourly Continuation — BRETT/USDT P21_34

**Symbol:** BRETT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1055 |
| net_profit_factor | 0.4137 |
| net_win_rate | 0.4322 |
| gross_profit_factor | 0.7606 |
| gross_win_rate | 0.4427 |
| sharpe_ratio | -8.8483 |
| sortino_ratio | -4.1533 |
| max_drawdown | 0.9932 |
| cagr | -0.8766 |
| net_avg_win | 15.3632 |
| net_avg_loss | -28.2735 |
| avg_hold_time_bars | 2.5782 |
| exposure | 0.1309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
