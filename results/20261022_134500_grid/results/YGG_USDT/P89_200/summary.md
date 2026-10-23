# EMA Hourly Continuation — YGG/USDT P89_200

**Symbol:** YGG/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.6253 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9183 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -2.8686 |
| sortino_ratio | -0.7963 |
| max_drawdown | 0.6332 |
| cagr | -0.3167 |
| net_avg_win | 54.7949 |
| net_avg_loss | -81.5622 |
| avg_hold_time_bars | 10.5949 |
| exposure | 0.1870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
