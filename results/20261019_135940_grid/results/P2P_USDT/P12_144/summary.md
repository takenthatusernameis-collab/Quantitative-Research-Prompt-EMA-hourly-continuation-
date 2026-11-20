# EMA Hourly Continuation — P2P/USDT P12_144

**Symbol:** P2P/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.6261 |
| net_win_rate | 0.4361 |
| gross_profit_factor | 0.7797 |
| gross_win_rate | 0.4361 |
| sharpe_ratio | -3.2364 |
| sortino_ratio | -1.0099 |
| max_drawdown | 0.6975 |
| cagr | -0.3788 |
| net_avg_win | 54.3131 |
| net_avg_loss | -67.0943 |
| avg_hold_time_bars | 28.3651 |
| exposure | 0.6356 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
