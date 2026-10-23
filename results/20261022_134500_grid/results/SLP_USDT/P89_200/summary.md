# EMA Hourly Continuation — SLP/USDT P89_200

**Symbol:** SLP/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.5520 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.8862 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -4.0278 |
| sortino_ratio | -1.1894 |
| max_drawdown | 0.7732 |
| cagr | -0.4461 |
| net_avg_win | 46.2574 |
| net_avg_loss | -71.0343 |
| avg_hold_time_bars | 10.3653 |
| exposure | 0.2115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
