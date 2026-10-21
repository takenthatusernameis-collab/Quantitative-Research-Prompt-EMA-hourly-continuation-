# EMA Hourly Continuation — UQC/USDT P89_200

**Symbol:** UQC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 175 |
| net_profit_factor | 0.3066 |
| net_win_rate | 0.2743 |
| gross_profit_factor | 0.4912 |
| gross_win_rate | 0.2971 |
| sharpe_ratio | -5.4302 |
| sortino_ratio | -1.0057 |
| max_drawdown | 0.7476 |
| cagr | -0.4207 |
| net_avg_win | 68.8540 |
| net_avg_loss | -84.8894 |
| avg_hold_time_bars | 52.6686 |
| exposure | 0.4172 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
