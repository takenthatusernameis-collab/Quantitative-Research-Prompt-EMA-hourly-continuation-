# EMA Hourly Continuation — FIL/USDT P8_89

**Symbol:** FIL/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 614 |
| net_profit_factor | 0.6162 |
| net_win_rate | 0.4739 |
| gross_profit_factor | 0.9406 |
| gross_win_rate | 0.4772 |
| sharpe_ratio | -3.9546 |
| sortino_ratio | -1.3683 |
| max_drawdown | 0.8272 |
| cagr | -0.4856 |
| net_avg_win | 44.7894 |
| net_avg_loss | -65.4816 |
| avg_hold_time_bars | 24.7590 |
| exposure | 0.6910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
