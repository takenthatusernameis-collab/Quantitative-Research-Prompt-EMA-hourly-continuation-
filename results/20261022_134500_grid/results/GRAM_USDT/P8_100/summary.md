# EMA Hourly Continuation — GRAM/USDT P8_100

**Symbol:** GRAM/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 721 |
| net_profit_factor | 0.4732 |
| net_win_rate | 0.4605 |
| gross_profit_factor | 0.8822 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -5.7351 |
| sortino_ratio | -2.1326 |
| max_drawdown | 0.9404 |
| cagr | -0.6612 |
| net_avg_win | 25.2749 |
| net_avg_loss | -45.5819 |
| avg_hold_time_bars | 19.8169 |
| exposure | 0.6495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
