# EMA Hourly Continuation — BCH/USDT P50_200

**Symbol:** BCH/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.5891 |
| net_win_rate | 0.4738 |
| gross_profit_factor | 0.9586 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -3.1798 |
| sortino_ratio | -0.8517 |
| max_drawdown | 0.6598 |
| cagr | -0.3360 |
| net_avg_win | 53.5371 |
| net_avg_loss | -81.8438 |
| avg_hold_time_bars | 24.4463 |
| exposure | 0.4034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
