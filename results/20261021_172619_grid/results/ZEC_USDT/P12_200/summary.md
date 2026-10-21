# EMA Hourly Continuation — ZEC/USDT P12_200

**Symbol:** ZEC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.8968 |
| net_win_rate | 0.5118 |
| gross_profit_factor | 1.0272 |
| gross_win_rate | 0.5118 |
| sharpe_ratio | -0.4763 |
| sortino_ratio | -0.1087 |
| max_drawdown | 0.1782 |
| cagr | -0.0516 |
| net_avg_win | 83.3616 |
| net_avg_loss | -97.4484 |
| avg_hold_time_bars | 65.3543 |
| exposure | 0.7545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
