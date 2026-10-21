# EMA Hourly Continuation — SSV/USDT P20_200

**Symbol:** SSV/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.7837 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9260 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -1.2231 |
| sortino_ratio | -0.2907 |
| max_drawdown | 0.3463 |
| cagr | -0.1262 |
| net_avg_win | 77.3766 |
| net_avg_loss | -91.9282 |
| avg_hold_time_bars | 52.4750 |
| exposure | 0.6649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
