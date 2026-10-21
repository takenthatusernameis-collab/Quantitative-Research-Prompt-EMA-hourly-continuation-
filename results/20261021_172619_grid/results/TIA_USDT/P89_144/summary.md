# EMA Hourly Continuation — TIA/USDT P89_144

**Symbol:** TIA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 239 |
| net_profit_factor | 0.7324 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.9108 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -1.5169 |
| sortino_ratio | -0.3345 |
| max_drawdown | 0.3616 |
| cagr | -0.1426 |
| net_avg_win | 76.9436 |
| net_avg_loss | -95.8062 |
| avg_hold_time_bars | 8.2887 |
| exposure | 0.0900 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
