# EMA Hourly Continuation — AVAX/USDT P55_144

**Symbol:** AVAX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 292 |
| net_profit_factor | 0.7176 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9182 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -1.8205 |
| sortino_ratio | -0.4434 |
| max_drawdown | 0.4310 |
| cagr | -0.1849 |
| net_avg_win | 72.8940 |
| net_avg_loss | -93.5605 |
| avg_hold_time_bars | 16.4212 |
| exposure | 0.2180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
