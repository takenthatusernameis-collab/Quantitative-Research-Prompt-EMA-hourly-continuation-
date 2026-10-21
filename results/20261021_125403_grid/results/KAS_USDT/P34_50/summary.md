# EMA Hourly Continuation — KAS/USDT P34_50

**Symbol:** KAS/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 184 |
| net_profit_factor | 0.7647 |
| net_win_rate | 0.5163 |
| gross_profit_factor | 1.0639 |
| gross_win_rate | 0.5163 |
| sharpe_ratio | -1.1189 |
| sortino_ratio | -0.2189 |
| max_drawdown | 0.2347 |
| cagr | -0.0949 |
| net_avg_win | 75.8120 |
| net_avg_loss | -105.8233 |
| avg_hold_time_bars | 5.9185 |
| exposure | 0.0495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
