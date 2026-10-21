# EMA Hourly Continuation — APE/USDT P12_200

**Symbol:** APE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.7598 |
| net_win_rate | 0.4781 |
| gross_profit_factor | 0.8983 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -1.2115 |
| sortino_ratio | -0.2605 |
| max_drawdown | 0.2844 |
| cagr | -0.1136 |
| net_avg_win | 75.8598 |
| net_avg_loss | -91.4479 |
| avg_hold_time_bars | 74.4561 |
| exposure | 0.7716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
