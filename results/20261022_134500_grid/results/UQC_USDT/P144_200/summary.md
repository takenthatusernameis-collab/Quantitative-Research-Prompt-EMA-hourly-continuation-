# EMA Hourly Continuation — UQC/USDT P144_200

**Symbol:** UQC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.2051 |
| net_win_rate | 0.2539 |
| gross_profit_factor | 0.4534 |
| gross_win_rate | 0.2978 |
| sharpe_ratio | -8.8014 |
| sortino_ratio | -2.3182 |
| max_drawdown | 0.9622 |
| cagr | -0.7271 |
| net_avg_win | 30.6522 |
| net_avg_loss | -50.8599 |
| avg_hold_time_bars | 14.8433 |
| exposure | 0.2143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
