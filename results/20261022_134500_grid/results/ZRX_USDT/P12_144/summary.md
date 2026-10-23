# EMA Hourly Continuation — ZRX/USDT P12_144

**Symbol:** ZRX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.6835 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9866 |
| gross_win_rate | 0.4950 |
| sharpe_ratio | -2.8016 |
| sortino_ratio | -0.8885 |
| max_drawdown | 0.6664 |
| cagr | -0.3436 |
| net_avg_win | 57.0572 |
| net_avg_loss | -79.9183 |
| avg_hold_time_bars | 28.8990 |
| exposure | 0.6634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
