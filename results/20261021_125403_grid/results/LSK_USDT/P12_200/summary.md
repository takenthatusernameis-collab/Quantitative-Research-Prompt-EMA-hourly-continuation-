# EMA Hourly Continuation — LSK/USDT P12_200

**Symbol:** LSK/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.8718 |
| net_win_rate | 0.5241 |
| gross_profit_factor | 1.0889 |
| gross_win_rate | 0.5241 |
| sharpe_ratio | -0.7683 |
| sortino_ratio | -0.2009 |
| max_drawdown | 0.3732 |
| cagr | -0.0912 |
| net_avg_win | 83.3742 |
| net_avg_loss | -105.3233 |
| avg_hold_time_bars | 48.0964 |
| exposure | 0.7258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
