# EMA Hourly Continuation — SNX/USDT P12_200

**Symbol:** SNX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.7270 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9846 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -2.2978 |
| sortino_ratio | -0.6701 |
| max_drawdown | 0.5640 |
| cagr | -0.2733 |
| net_avg_win | 70.1308 |
| net_avg_loss | -91.6686 |
| avg_hold_time_bars | 35.8840 |
| exposure | 0.6999 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
