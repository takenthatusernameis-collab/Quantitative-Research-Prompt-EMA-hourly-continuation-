# EMA Hourly Continuation — YFI/USDT P20_144

**Symbol:** YFI/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.7896 |
| net_win_rate | 0.5164 |
| gross_profit_factor | 1.0630 |
| gross_win_rate | 0.5164 |
| sharpe_ratio | -1.5448 |
| sortino_ratio | -0.4566 |
| max_drawdown | 0.4746 |
| cagr | -0.1901 |
| net_avg_win | 70.3505 |
| net_avg_loss | -95.1519 |
| avg_hold_time_bars | 29.0469 |
| exposure | 0.5599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
