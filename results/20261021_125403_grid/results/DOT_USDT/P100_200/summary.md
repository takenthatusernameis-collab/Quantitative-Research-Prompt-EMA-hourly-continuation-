# EMA Hourly Continuation — DOT/USDT P100_200

**Symbol:** DOT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 247 |
| net_profit_factor | 0.8214 |
| net_win_rate | 0.5263 |
| gross_profit_factor | 1.0931 |
| gross_win_rate | 0.5263 |
| sharpe_ratio | -0.8843 |
| sortino_ratio | -0.2004 |
| max_drawdown | 0.2437 |
| cagr | -0.0892 |
| net_avg_win | 74.0359 |
| net_avg_loss | -100.1432 |
| avg_hold_time_bars | 10.8866 |
| exposure | 0.1222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
