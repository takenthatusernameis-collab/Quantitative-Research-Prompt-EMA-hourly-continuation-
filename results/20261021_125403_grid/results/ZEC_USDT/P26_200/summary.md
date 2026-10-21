# EMA Hourly Continuation — ZEC/USDT P26_200

**Symbol:** ZEC/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.9750 |
| net_win_rate | 0.5311 |
| gross_profit_factor | 1.1301 |
| gross_win_rate | 0.5311 |
| sharpe_ratio | -0.0852 |
| sortino_ratio | -0.0203 |
| max_drawdown | 0.2041 |
| cagr | -0.0142 |
| net_avg_win | 94.9979 |
| net_avg_loss | -110.3691 |
| avg_hold_time_bars | 45.3846 |
| exposure | 0.5632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
