# EMA Hourly Continuation — PEPE/USDT P89_144

**Symbol:** PEPE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.7927 |
| net_win_rate | 0.5040 |
| gross_profit_factor | 1.0153 |
| gross_win_rate | 0.5040 |
| sharpe_ratio | -1.1565 |
| sortino_ratio | -0.2613 |
| max_drawdown | 0.2887 |
| cagr | -0.1137 |
| net_avg_win | 80.0134 |
| net_avg_loss | -102.5797 |
| avg_hold_time_bars | 7.7903 |
| exposure | 0.0878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
