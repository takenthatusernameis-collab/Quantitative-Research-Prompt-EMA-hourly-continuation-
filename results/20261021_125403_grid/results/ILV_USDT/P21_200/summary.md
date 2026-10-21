# EMA Hourly Continuation — ILV/USDT P21_200

**Symbol:** ILV/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.9720 |
| net_win_rate | 0.5394 |
| gross_profit_factor | 1.1646 |
| gross_win_rate | 0.5394 |
| sharpe_ratio | -0.1060 |
| sortino_ratio | -0.0273 |
| max_drawdown | 0.1378 |
| cagr | -0.0181 |
| net_avg_win | 90.9503 |
| net_avg_loss | -109.5872 |
| avg_hold_time_bars | 43.4132 |
| exposure | 0.6255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
