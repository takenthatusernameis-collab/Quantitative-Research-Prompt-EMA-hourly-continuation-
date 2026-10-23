# EMA Hourly Continuation — TRADE/USDT P55_100

**Symbol:** TRADE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.4052 |
| net_win_rate | 0.3878 |
| gross_profit_factor | 0.6445 |
| gross_win_rate | 0.3898 |
| sharpe_ratio | -6.1937 |
| sortino_ratio | -1.9238 |
| max_drawdown | 0.9129 |
| cagr | -0.6191 |
| net_avg_win | 32.6850 |
| net_avg_loss | -51.0823 |
| avg_hold_time_bars | 6.8102 |
| exposure | 0.1517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
