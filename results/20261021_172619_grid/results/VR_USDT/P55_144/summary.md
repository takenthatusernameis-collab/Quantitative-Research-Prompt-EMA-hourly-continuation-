# EMA Hourly Continuation — VR/USDT P55_144

**Symbol:** VR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.5729 |
| net_win_rate | 0.4173 |
| gross_profit_factor | 0.6953 |
| gross_win_rate | 0.4173 |
| sharpe_ratio | -2.7670 |
| sortino_ratio | -0.6501 |
| max_drawdown | 0.5300 |
| cagr | -0.2597 |
| net_avg_win | 61.2888 |
| net_avg_loss | -76.6011 |
| avg_hold_time_bars | 16.7050 |
| exposure | 0.2111 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
