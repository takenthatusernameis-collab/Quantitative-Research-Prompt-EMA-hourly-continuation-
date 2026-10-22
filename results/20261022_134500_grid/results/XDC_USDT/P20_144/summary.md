# EMA Hourly Continuation — XDC/USDT P20_144

**Symbol:** XDC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.3734 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.7772 |
| gross_win_rate | 0.4892 |
| sharpe_ratio | -5.8815 |
| sortino_ratio | -2.1363 |
| max_drawdown | 0.9394 |
| cagr | -0.6703 |
| net_avg_win | 17.3650 |
| net_avg_loss | -40.3646 |
| avg_hold_time_bars | 14.4069 |
| exposure | 0.4538 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
