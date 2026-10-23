# EMA Hourly Continuation — SKL/USDT P12_144

**Symbol:** SKL/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.8103 |
| net_win_rate | 0.5136 |
| gross_profit_factor | 1.1121 |
| gross_win_rate | 0.5177 |
| sharpe_ratio | -1.7917 |
| sortino_ratio | -0.5531 |
| max_drawdown | 0.6327 |
| cagr | -0.2330 |
| net_avg_win | 84.4625 |
| net_avg_loss | -110.0500 |
| avg_hold_time_bars | 31.7787 |
| exposure | 0.6919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
