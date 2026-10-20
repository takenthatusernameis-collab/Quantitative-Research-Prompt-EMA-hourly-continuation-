# EMA Hourly Continuation — YFI/USDT P12_26

**Symbol:** YFI/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1513 |
| net_profit_factor | 0.2495 |
| net_win_rate | 0.4025 |
| gross_profit_factor | 0.7977 |
| gross_win_rate | 0.4435 |
| sharpe_ratio | -14.0598 |
| sortino_ratio | -7.8193 |
| max_drawdown | 1.0000 |
| cagr | -0.9821 |
| net_avg_win | 5.4586 |
| net_avg_loss | -14.7388 |
| avg_hold_time_bars | 3.1454 |
| exposure | 0.2153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
