# EMA Hourly Continuation — DEXE/USDT P12_144

**Symbol:** DEXE/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.8354 |
| net_win_rate | 0.5322 |
| gross_profit_factor | 1.1415 |
| gross_win_rate | 0.5396 |
| sharpe_ratio | -0.9648 |
| sortino_ratio | -0.2767 |
| max_drawdown | 0.3980 |
| cagr | -0.1242 |
| net_avg_win | 66.8264 |
| net_avg_loss | -91.0014 |
| avg_hold_time_bars | 40.4134 |
| exposure | 0.7421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
