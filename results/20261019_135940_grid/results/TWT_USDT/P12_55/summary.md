# EMA Hourly Continuation — TWT/USDT P12_55

**Symbol:** TWT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1072 |
| net_profit_factor | 0.4724 |
| net_win_rate | 0.4739 |
| gross_profit_factor | 0.9197 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -6.6916 |
| sortino_ratio | -3.0738 |
| max_drawdown | 0.9787 |
| cagr | -0.7811 |
| net_avg_win | 17.2398 |
| net_avg_loss | -32.8676 |
| avg_hold_time_bars | 8.0429 |
| exposure | 0.3919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
