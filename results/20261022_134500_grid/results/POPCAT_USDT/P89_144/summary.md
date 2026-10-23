# EMA Hourly Continuation — POPCAT/USDT P89_144

**Symbol:** POPCAT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.6333 |
| net_win_rate | 0.4717 |
| gross_profit_factor | 0.8960 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -3.4674 |
| sortino_ratio | -1.1262 |
| max_drawdown | 0.6927 |
| cagr | -0.4170 |
| net_avg_win | 54.7835 |
| net_avg_loss | -77.2509 |
| avg_hold_time_bars | 5.2065 |
| exposure | 0.1265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
