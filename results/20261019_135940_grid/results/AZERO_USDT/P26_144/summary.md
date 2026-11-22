# EMA Hourly Continuation — AZERO/USDT P26_144

**Symbol:** AZERO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.6903 |
| net_win_rate | 0.4730 |
| gross_profit_factor | 0.9282 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -2.6427 |
| sortino_ratio | -0.8015 |
| max_drawdown | 0.6475 |
| cagr | -0.3142 |
| net_avg_win | 62.4545 |
| net_avg_loss | -81.2097 |
| avg_hold_time_bars | 23.2786 |
| exposure | 0.4877 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
