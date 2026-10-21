# EMA Hourly Continuation — KSM/USDT P12_144

**Symbol:** KSM/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.7412 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.9099 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -1.8260 |
| sortino_ratio | -0.4720 |
| max_drawdown | 0.4648 |
| cagr | -0.1961 |
| net_avg_win | 76.9869 |
| net_avg_loss | -93.7169 |
| avg_hold_time_bars | 48.0121 |
| exposure | 0.7224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
