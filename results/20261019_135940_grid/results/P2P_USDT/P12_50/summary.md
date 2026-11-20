# EMA Hourly Continuation — P2P/USDT P12_50

**Symbol:** P2P/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1006 |
| net_profit_factor | 0.3894 |
| net_win_rate | 0.3588 |
| gross_profit_factor | 0.5883 |
| gross_win_rate | 0.3598 |
| sharpe_ratio | -8.8160 |
| sortino_ratio | -3.8912 |
| max_drawdown | 0.9919 |
| cagr | -0.8533 |
| net_avg_win | 17.5252 |
| net_avg_loss | -25.1875 |
| avg_hold_time_bars | 8.0517 |
| exposure | 0.3682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
