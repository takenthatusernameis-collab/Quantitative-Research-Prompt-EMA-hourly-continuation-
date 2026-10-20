# EMA Hourly Continuation — TFUEL/USDT P21_89

**Symbol:** TFUEL/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 866 |
| net_profit_factor | 0.4827 |
| net_win_rate | 0.4122 |
| gross_profit_factor | 0.7790 |
| gross_win_rate | 0.4249 |
| sharpe_ratio | -7.5845 |
| sortino_ratio | -3.1166 |
| max_drawdown | 0.9801 |
| cagr | -0.7849 |
| net_avg_win | 25.5936 |
| net_avg_loss | -37.1899 |
| avg_hold_time_bars | 8.8383 |
| exposure | 0.3464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
