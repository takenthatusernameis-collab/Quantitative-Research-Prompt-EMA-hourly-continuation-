# EMA Hourly Continuation — QNT/USDT P26_200

**Symbol:** QNT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.6760 |
| net_win_rate | 0.4927 |
| gross_profit_factor | 0.9981 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -2.6025 |
| sortino_ratio | -0.8019 |
| max_drawdown | 0.6467 |
| cagr | -0.3156 |
| net_avg_win | 54.2930 |
| net_avg_loss | -78.0046 |
| avg_hold_time_bars | 25.3048 |
| exposure | 0.5510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
