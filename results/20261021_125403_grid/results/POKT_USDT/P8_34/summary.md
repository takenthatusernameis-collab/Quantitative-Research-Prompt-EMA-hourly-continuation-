# EMA Hourly Continuation — POKT/USDT P8_34

**Symbol:** POKT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 755 |
| net_profit_factor | 0.5948 |
| net_win_rate | 0.4159 |
| gross_profit_factor | 0.7726 |
| gross_win_rate | 0.4159 |
| sharpe_ratio | -5.2127 |
| sortino_ratio | -2.0191 |
| max_drawdown | 0.9081 |
| cagr | -0.6085 |
| net_avg_win | 42.3586 |
| net_avg_loss | -50.7065 |
| avg_hold_time_bars | 8.5762 |
| exposure | 0.2930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
