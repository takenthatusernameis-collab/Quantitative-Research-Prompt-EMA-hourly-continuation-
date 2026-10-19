# EMA Hourly Continuation — FET/USDT P144_200

**Symbol:** FET/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.6118 |
| net_win_rate | 0.4944 |
| gross_profit_factor | 1.0239 |
| gross_win_rate | 0.5028 |
| sharpe_ratio | -2.9278 |
| sortino_ratio | -0.7822 |
| max_drawdown | 0.6181 |
| cagr | -0.3120 |
| net_avg_win | 54.5376 |
| net_avg_loss | -87.1606 |
| avg_hold_time_bars | 4.0983 |
| exposure | 0.0663 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
