# EMA Hourly Continuation — RPL/USDT P12_34

**Symbol:** RPL/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 742 |
| net_profit_factor | 0.7116 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9642 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -3.3058 |
| sortino_ratio | -1.2839 |
| max_drawdown | 0.7764 |
| cagr | -0.4462 |
| net_avg_win | 53.5472 |
| net_avg_loss | -69.7769 |
| avg_hold_time_bars | 7.2938 |
| exposure | 0.2449 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
