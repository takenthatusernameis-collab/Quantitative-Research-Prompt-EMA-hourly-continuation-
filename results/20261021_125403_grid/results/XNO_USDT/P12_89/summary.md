# EMA Hourly Continuation — XNO/USDT P12_89

**Symbol:** XNO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.7241 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.8905 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -2.7597 |
| sortino_ratio | -0.9509 |
| max_drawdown | 0.6793 |
| cagr | -0.3545 |
| net_avg_win | 64.3436 |
| net_avg_loss | -76.4892 |
| avg_hold_time_bars | 17.2908 |
| exposure | 0.4621 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
