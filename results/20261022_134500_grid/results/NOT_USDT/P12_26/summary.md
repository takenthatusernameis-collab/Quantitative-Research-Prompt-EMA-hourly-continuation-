# EMA Hourly Continuation — NOT/USDT P12_26

**Symbol:** NOT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1406 |
| net_profit_factor | 0.5177 |
| net_win_rate | 0.4388 |
| gross_profit_factor | 0.9406 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -10.3154 |
| sortino_ratio | -5.5278 |
| max_drawdown | 0.9989 |
| cagr | -0.9390 |
| net_avg_win | 17.3749 |
| net_avg_loss | -26.2473 |
| avg_hold_time_bars | 2.8250 |
| exposure | 0.1866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
