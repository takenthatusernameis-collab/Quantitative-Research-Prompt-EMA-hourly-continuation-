# EMA Hourly Continuation — COMP/USDT P20_89

**Symbol:** COMP/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 568 |
| net_profit_factor | 0.6797 |
| net_win_rate | 0.4877 |
| gross_profit_factor | 0.9118 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -2.6398 |
| sortino_ratio | -0.8978 |
| max_drawdown | 0.6809 |
| cagr | -0.3386 |
| net_avg_win | 49.4683 |
| net_avg_loss | -69.2827 |
| avg_hold_time_bars | 15.3028 |
| exposure | 0.3951 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
