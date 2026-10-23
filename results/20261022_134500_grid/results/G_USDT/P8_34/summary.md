# EMA Hourly Continuation — G/USDT P8_34

**Symbol:** G/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1007 |
| net_profit_factor | 0.5256 |
| net_win_rate | 0.4638 |
| gross_profit_factor | 0.9015 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -6.6822 |
| sortino_ratio | -3.2280 |
| max_drawdown | 0.9646 |
| cagr | -0.7846 |
| net_avg_win | 22.8733 |
| net_avg_loss | -37.6386 |
| avg_hold_time_bars | 7.0864 |
| exposure | 0.3752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
