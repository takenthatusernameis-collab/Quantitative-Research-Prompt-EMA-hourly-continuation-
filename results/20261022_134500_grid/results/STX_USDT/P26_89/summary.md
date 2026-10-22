# EMA Hourly Continuation — STX/USDT P26_89

**Symbol:** STX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.5783 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.8586 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -4.5592 |
| sortino_ratio | -1.6836 |
| max_drawdown | 0.8741 |
| cagr | -0.5503 |
| net_avg_win | 37.3767 |
| net_avg_loss | -55.5514 |
| avg_hold_time_bars | 9.8372 |
| exposure | 0.3063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
