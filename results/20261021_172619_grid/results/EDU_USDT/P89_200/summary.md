# EMA Hourly Continuation — EDU/USDT P89_200

**Symbol:** EDU/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 319 |
| net_profit_factor | 0.6707 |
| net_win_rate | 0.4577 |
| gross_profit_factor | 0.8304 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -2.1632 |
| sortino_ratio | -0.5475 |
| max_drawdown | 0.4852 |
| cagr | -0.2234 |
| net_avg_win | 65.7848 |
| net_avg_loss | -82.7772 |
| avg_hold_time_bars | 13.4138 |
| exposure | 0.1936 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
