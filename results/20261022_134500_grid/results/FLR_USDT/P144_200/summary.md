# EMA Hourly Continuation — FLR/USDT P144_200

**Symbol:** FLR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.3845 |
| net_win_rate | 0.4319 |
| gross_profit_factor | 0.8376 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -6.4759 |
| sortino_ratio | -2.0046 |
| max_drawdown | 0.9253 |
| cagr | -0.6393 |
| net_avg_win | 27.9803 |
| net_avg_loss | -55.3196 |
| avg_hold_time_bars | 4.3082 |
| exposure | 0.0934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
