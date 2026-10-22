# EMA Hourly Continuation — STX/USDT P89_200

**Symbol:** STX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.6586 |
| net_win_rate | 0.5173 |
| gross_profit_factor | 1.1102 |
| gross_win_rate | 0.5307 |
| sharpe_ratio | -2.3045 |
| sortino_ratio | -0.6182 |
| max_drawdown | 0.5526 |
| cagr | -0.2642 |
| net_avg_win | 53.5730 |
| net_avg_loss | -87.1882 |
| avg_hold_time_bars | 11.8987 |
| exposure | 0.2019 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
