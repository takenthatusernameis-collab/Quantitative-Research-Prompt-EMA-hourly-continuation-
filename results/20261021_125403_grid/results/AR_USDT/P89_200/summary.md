# EMA Hourly Continuation — AR/USDT P89_200

**Symbol:** AR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 262 |
| net_profit_factor | 0.7155 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.8725 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -1.7777 |
| sortino_ratio | -0.4086 |
| max_drawdown | 0.4163 |
| cagr | -0.1713 |
| net_avg_win | 78.1879 |
| net_avg_loss | -93.7770 |
| avg_hold_time_bars | 14.6489 |
| exposure | 0.1745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
